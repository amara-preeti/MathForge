import React, { useState } from 'react';
import Plot from 'react-plotly.js';

export const PlottingStudio: React.FC = () => {
    const [expression, setExpression] = useState('sin(x) * exp(-0.1 * x)');
    const [xMin, setXMin] = useState('-10');
    const [xMax, setXMax] = useState('10');
    const [plotData, setPlotData] = useState<{x: number[], y: (number|null)[]} | null>(null);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handlePlot = async () => {
        setLoading(true);
        setError(null);
        try {
            const res = await fetch(`http://127.0.0.1:8000/api/plotting/generate_2d`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    expression, 
                    x_min: parseFloat(xMin), 
                    x_max: parseFloat(xMax),
                    points: 500
                })
            });
            const data = await res.json();
            
            if (data.error) {
                setError(data.error);
            } else {
                setPlotData(data);
            }
        } catch (e) {
            setError('Network error or backend offline.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg border border-gray-700 h-full flex flex-col">
            <h2 className="text-2xl font-bold mb-4 text-pink-300">Plotting Studio</h2>
            
            <div className="flex space-x-4 mb-6">
                <div className="flex-1">
                    <label className="block text-gray-400 mb-1">Function f(x)</label>
                    <input 
                        type="text" 
                        value={expression} 
                        onChange={(e) => setExpression(e.target.value)} 
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-pink-500 focus:outline-none"
                    />
                </div>
                
                <div className="w-24">
                    <label className="block text-gray-400 mb-1">X Min</label>
                    <input 
                        type="number" 
                        value={xMin} 
                        onChange={(e) => setXMin(e.target.value)} 
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-pink-500 focus:outline-none"
                    />
                </div>

                <div className="w-24">
                    <label className="block text-gray-400 mb-1">X Max</label>
                    <input 
                        type="number" 
                        value={xMax} 
                        onChange={(e) => setXMax(e.target.value)} 
                        className="w-full bg-gray-900 border border-gray-600 rounded p-2 text-white font-mono focus:border-pink-500 focus:outline-none"
                    />
                </div>

                <div className="flex items-end">
                    <button 
                        onClick={handlePlot}
                        disabled={loading}
                        className="bg-pink-600 hover:bg-pink-500 text-white font-bold py-2 px-6 rounded transition h-10"
                    >
                        {loading ? 'Plotting...' : 'Plot'}
                    </button>
                </div>
            </div>

            {error && (
                <div className="mb-4 p-4 bg-red-900/50 border border-red-700 rounded text-red-300">
                    {error}
                </div>
            )}

            <div className="flex-1 bg-white rounded flex items-center justify-center overflow-hidden min-h-[400px]">
                {plotData ? (
                    <Plot
                        data={[
                            {
                                x: plotData.x,
                                y: plotData.y,
                                type: 'scatter',
                                mode: 'lines',
                                marker: {color: 'hotpink'},
                                name: expression
                            },
                        ]}
                        layout={{ 
                            title: `Plot of ${expression}`,
                            autosize: true,
                            margin: { l: 50, r: 50, b: 50, t: 50, pad: 4 }
                        }}
                        useResizeHandler={true}
                        style={{width: "100%", height: "100%"}}
                    />
                ) : (
                    <span className="text-gray-400">Enter a function and hit Plot to visualize.</span>
                )}
            </div>
        </div>
    );
};
