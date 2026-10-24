import React, { useState } from 'react';
import 'katex/dist/katex.min.css';
import { BlockMath } from 'react-katex';

export const MatrixLab: React.FC = () => {
    const [matrixStr, setMatrixStr] = useState('[[1, 2], [3, 4]]');
    const [operation, setOperation] = useState('properties');
    const [result, setResult] = useState<any>(null);
    const [loading, setLoading] = useState(false);

    const handleCalculate = async () => {
        setLoading(true);
        setResult(null);
        try {
            const matrix = JSON.parse(matrixStr); // Simple parsing for now
            const res = await fetch(`http://127.0.0.1:8000/api/matrix/${operation}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ matrix })
            });
            const data = await res.json();
            setResult(data);
        } catch (e) {
            setResult({ detail: 'Invalid matrix format. Use JSON format like [[1,2],[3,4]] or Network error.' });
        } finally {
            setLoading(false);
        }
    };

    const renderMatrixLatex = (mat: number[][]) => {
        if (!mat || !mat.length) return '';
        const rows = mat.map(row => row.join(' & ')).join(' \\\\ ');
        return `\\begin{bmatrix} ${rows} \\end{bmatrix}`;
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg border border-gray-700">
            <h2 className="text-2xl font-bold mb-4 text-yellow-300">Matrix Lab</h2>
            
            <div className="flex flex-col space-y-4">
                <div>
                    <label className="block text-gray-400 mb-1">Matrix (JSON format)</label>
                    <textarea 
                        value={matrixStr} 
                        onChange={(e) => setMatrixStr(e.target.value)} 
                        rows={4}
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-yellow-500 focus:outline-none"
                    />
                </div>
                
                <div className="flex space-x-4">
                    <div className="flex-1">
                        <label className="block text-gray-400 mb-1">Operation</label>
                        <select 
                            value={operation}
                            onChange={(e) => setOperation(e.target.value)}
                            className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-yellow-500 focus:outline-none"
                        >
                            <option value="properties">Properties (Det, Rank, Trace, Inv)</option>
                            <option value="eigen">Eigenvalues & Eigenvectors</option>
                        </select>
                    </div>
                </div>

                <button 
                    onClick={handleCalculate}
                    disabled={loading}
                    className="bg-yellow-600 hover:bg-yellow-500 text-white font-bold py-2 px-4 rounded transition"
                >
                    {loading ? 'Computing...' : 'Calculate'}
                </button>
            </div>

            {result && (
                <div className="mt-6 p-4 bg-gray-900 rounded border border-gray-700">
                    <h3 className="text-lg font-semibold text-gray-300 mb-2">Result:</h3>
                    {result.detail ? (
                        <p className="text-red-400 font-mono text-sm break-words">{result.detail}</p>
                    ) : (
                        <div className="text-xl py-4 bg-black rounded overflow-auto p-4 space-y-4">
                            {operation === 'properties' && (
                                <>
                                    <p className="text-gray-300 text-sm">Shape: {result.shape.join(' × ')}</p>
                                    <p className="text-gray-300 text-sm">Determinant: {result.determinant !== null ? result.determinant.toFixed(4) : 'N/A'}</p>
                                    <p className="text-gray-300 text-sm">Rank: {result.rank}</p>
                                    <p className="text-gray-300 text-sm">Trace: {result.trace !== null ? result.trace : 'N/A'}</p>
                                    {result.inverse && (
                                        <div className="mt-4">
                                            <p className="text-gray-300 text-sm mb-2">Inverse:</p>
                                            <BlockMath math={renderMatrixLatex(result.inverse)} />
                                        </div>
                                    )}
                                </>
                            )}
                            {operation === 'eigen' && (
                                <>
                                    <div className="mb-4">
                                        <p className="text-gray-300 text-sm mb-2">Eigenvalues:</p>
                                        <pre className="text-blue-300 text-sm">{result.eigenvalues.join(', ')}</pre>
                                    </div>
                                    <div>
                                        <p className="text-gray-300 text-sm mb-2">Eigenvectors (columns):</p>
                                        <pre className="text-green-300 text-sm">{JSON.stringify(result.eigenvectors, null, 2)}</pre>
                                    </div>
                                </>
                            )}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};
