import React, { useState } from 'react';
import 'katex/dist/katex.min.css';
import { BlockMath } from 'react-katex';

export const CalculusLab: React.FC = () => {
    const [expression, setExpression] = useState('sin(x)/x');
    const [operation, setOperation] = useState('limit');
    const [variable, setVariable] = useState('x');
    const [value, setValue] = useState('0'); // For limit point or taylor expansion point
    const [degree, setDegree] = useState('5'); // For taylor series
    const [result, setResult] = useState<{result?: string, latex?: string, error?: string} | null>(null);
    const [loading, setLoading] = useState(false);

    const handleCalculate = async () => {
        setLoading(true);
        setResult(null);
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/calculus/${operation}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    expression, 
                    variable: variable || null, 
                    value: value || null,
                    degree: parseInt(degree) || 5
                })
            });
            const data = await res.json();
            setResult(data);
        } catch (e) {
            setResult({ error: 'Network error or backend offline.' });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg border border-gray-700">
            <h2 className="text-2xl font-bold mb-4 text-purple-300">Calculus Lab</h2>
            
            <div className="flex flex-col space-y-4">
                <div>
                    <label className="block text-gray-400 mb-1">Expression (SymPy syntax)</label>
                    <input 
                        type="text" 
                        value={expression} 
                        onChange={(e) => setExpression(e.target.value)} 
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-purple-500 focus:outline-none"
                    />
                </div>
                
                <div className="flex space-x-4">
                    <div className="flex-1">
                        <label className="block text-gray-400 mb-1">Operation</label>
                        <select 
                            value={operation}
                            onChange={(e) => setOperation(e.target.value)}
                            className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-purple-500 focus:outline-none"
                        >
                            <option value="limit">Limit</option>
                            <option value="taylor">Taylor Series</option>
                        </select>
                    </div>
                    
                    <div className="w-24">
                        <label className="block text-gray-400 mb-1">Variable</label>
                        <input 
                            type="text" 
                            value={variable} 
                            onChange={(e) => setVariable(e.target.value)} 
                            className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-purple-500 focus:outline-none"
                        />
                    </div>

                    <div className="w-24">
                        <label className="block text-gray-400 mb-1">{operation === 'limit' ? 'Approaching' : 'Around'}</label>
                        <input 
                            type="text" 
                            value={value} 
                            onChange={(e) => setValue(e.target.value)} 
                            className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-purple-500 focus:outline-none"
                        />
                    </div>

                    {operation === 'taylor' && (
                        <div className="w-24">
                            <label className="block text-gray-400 mb-1">Degree</label>
                            <input 
                                type="number" 
                                value={degree} 
                                onChange={(e) => setDegree(e.target.value)} 
                                className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-purple-500 focus:outline-none"
                            />
                        </div>
                    )}
                </div>

                <button 
                    onClick={handleCalculate}
                    disabled={loading}
                    className="bg-purple-600 hover:bg-purple-500 text-white font-bold py-2 px-4 rounded transition"
                >
                    {loading ? 'Computing...' : 'Calculate'}
                </button>
            </div>

            {result && (
                <div className="mt-6 p-4 bg-gray-900 rounded border border-gray-700">
                    <h3 className="text-lg font-semibold text-gray-300 mb-2">Result:</h3>
                    {result.error ? (
                        <p className="text-red-400 font-mono text-sm break-words">{result.error}</p>
                    ) : (
                        <div className="text-xl text-center py-4 bg-black rounded overflow-auto">
                            {result.latex ? <BlockMath math={result.latex} /> : <p className="font-mono">{result.result}</p>}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};
