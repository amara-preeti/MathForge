import React, { useState } from 'react';

type Cell = {
    id: string;
    type: 'code' | 'markdown';
    content: string;
    output?: string;
    error?: string;
    result?: string;
};

export const NotebookLab: React.FC = () => {
    const [cells, setCells] = useState<Cell[]>([
        { id: '1', type: 'markdown', content: '# Welcome to MathForge Notebooks\n\nRun local Python code effortlessly.' },
        { id: '2', type: 'code', content: 'import numpy as np\nx = np.array([1, 2, 3])\nx * 2' }
    ]);
    const [running, setRunning] = useState<string | null>(null);

    const runCell = async (id: string, content: string, type: 'code' | 'markdown') => {
        if (type !== 'code') return;
        setRunning(id);
        
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/notebook/execute`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code: content })
            });
            const data = await res.json();
            
            setCells(cells.map(c => 
                c.id === id ? { ...c, output: data.stdout, error: data.stderr, result: data.result } : c
            ));
        } catch (e) {
            setCells(cells.map(c => 
                c.id === id ? { ...c, error: 'Network error or backend offline.' } : c
            ));
        } finally {
            setRunning(null);
        }
    };

    const addCell = (type: 'code' | 'markdown') => {
        setCells([...cells, { id: Date.now().toString(), type, content: '' }]);
    };

    const updateCellContent = (id: string, content: string) => {
        setCells(cells.map(c => c.id === id ? { ...c, content } : c));
    };

    const resetKernel = async () => {
        await fetch(`http://127.0.0.1:8000/api/notebook/reset`, { method: 'POST' });
        setCells(cells.map(c => ({...c, output: '', error: '', result: ''})));
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg border border-gray-700 min-h-full">
            <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold text-blue-300">Python Notebook Engine</h2>
                <div className="space-x-2">
                    <button onClick={() => addCell('code')} className="bg-gray-700 hover:bg-gray-600 px-3 py-1 rounded text-sm">+ Code</button>
                    <button onClick={() => addCell('markdown')} className="bg-gray-700 hover:bg-gray-600 px-3 py-1 rounded text-sm">+ Markdown</button>
                    <button onClick={resetKernel} className="bg-red-900 hover:bg-red-800 text-red-200 px-3 py-1 rounded text-sm font-bold">Restart Kernel</button>
                </div>
            </div>

            <div className="space-y-6">
                {cells.map((cell, idx) => (
                    <div key={cell.id} className="border border-gray-700 rounded-lg overflow-hidden flex flex-col">
                        <div className="bg-gray-900 p-2 flex justify-between items-center border-b border-gray-700">
                            <span className="text-xs text-gray-500 font-mono uppercase tracking-wider">{cell.type === 'code' ? `In [${idx+1}]` : 'Markdown'}</span>
                            {cell.type === 'code' && (
                                <button 
                                    onClick={() => runCell(cell.id, cell.content, cell.type)}
                                    disabled={running === cell.id}
                                    className="text-green-400 hover:text-green-300 font-bold text-sm"
                                >
                                    {running === cell.id ? 'Running...' : 'Run ▶'}
                                </button>
                            )}
                        </div>
                        
                        <textarea 
                            value={cell.content}
                            onChange={(e) => updateCellContent(cell.id, e.target.value)}
                            className="w-full bg-gray-950 text-white font-mono p-4 outline-none resize-none focus:bg-black transition min-h-[100px]"
                        />

                        {cell.type === 'code' && (cell.output || cell.error || cell.result) && (
                            <div className="bg-gray-900 border-t border-gray-700 p-4 font-mono text-sm">
                                {cell.output && <div className="text-gray-300 whitespace-pre-wrap">{cell.output}</div>}
                                {cell.error && <div className="text-red-400 whitespace-pre-wrap mt-2">{cell.error}</div>}
                                {cell.result && <div className="text-yellow-300 mt-2">Out: {cell.result}</div>}
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
};
