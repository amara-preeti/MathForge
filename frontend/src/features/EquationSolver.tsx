import React, { useState } from 'react';
import 'katex/dist/katex.min.css';
import { BlockMath } from 'react-katex';

export const EquationSolver: React.FC = () => {
    const [equation, setEquation] = useState('x^2 - 5*x + 6 = 0');
    const [variable, setVariable] = useState('x');
    const [result, setResult] = useState<{solutions?: string[], latex_solutions?: string[], error?: string} | null>(null);
    const [loading, setLoading] = useState(false);

    const handleCalculate = async () => {
        setLoading(true);
        setResult(null);
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/equations/solve`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ equation, variable: variable || null })
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
            <h2 className="text-2xl font-bold mb-4 text-green-300">Equation Solver</h2>
            
            <div className="flex flex-col space-y-4">
                <div>
                    <label className="block text-gray-400 mb-1">Equation</label>
                    <input 
                        type="text" 
                        value={equation} 
                        onChange={(e) => setEquation(e.target.value)} 
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-green-500 focus:outline-none"
                    />
                </div>
                
                <div className="w-24">
                    <label className="block text-gray-400 mb-1">Variable</label>
                    <input 
                        type="text" 
                        value={variable} 
                        onChange={(e) => setVariable(e.target.value)} 
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-green-500 focus:outline-none"
                    />
                </div>

                <button 
                    onClick={handleCalculate}
                    disabled={loading}
                    className="bg-green-600 hover:bg-green-500 text-white font-bold py-2 px-4 rounded transition"
                >
                    {loading ? 'Solving...' : 'Solve'}
                </button>
            </div>

            {result && (
                <div className="mt-6 p-4 bg-gray-900 rounded border border-gray-700">
                    <h3 className="text-lg font-semibold text-gray-300 mb-2">Solutions:</h3>
                    {result.error ? (
                        <p className="text-red-400 font-mono text-sm break-words">{result.error}</p>
                    ) : (
                        <div className="text-xl text-center py-4 bg-black rounded overflow-auto space-y-2">
                            {result.latex_solutions && result.latex_solutions.length > 0 ? (
                                result.latex_solutions.map((sol, idx) => (
                                    <div key={idx}>
                                        <BlockMath math={`${variable} = ${sol}`} />
                                    </div>
                                ))
                            ) : (
                                <p className="text-gray-400">No solutions found.</p>
                            )}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};
