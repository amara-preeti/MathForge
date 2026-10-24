import React, { useState, useEffect } from 'react';

export const ProjectManager: React.FC = () => {
    const [projects, setProjects] = useState<any[]>([]);
    const [newProjName, setNewProjName] = useState('');
    const [loading, setLoading] = useState(true);

    const loadProjects = async () => {
        setLoading(true);
        try {
            const res = await fetch('http://127.0.0.1:8000/api/projects/');
            const data = await res.json();
            setProjects(data);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        loadProjects();
    }, []);

    const createProject = async () => {
        if (!newProjName) return;
        try {
            await fetch('http://127.0.0.1:8000/api/projects/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name: newProjName, description: "A new MathForge project." })
            });
            setNewProjName('');
            loadProjects();
        } catch (e) {
            console.error(e);
        }
    };

    return (
        <div className="bg-gray-800 p-6 rounded-lg shadow-lg border border-gray-700 min-h-[400px]">
            <h2 className="text-2xl font-bold mb-4 text-cyan-300">Project Manager</h2>
            
            <div className="flex space-x-4 mb-6">
                <input 
                    type="text" 
                    value={newProjName}
                    onChange={(e) => setNewProjName(e.target.value)}
                    placeholder="New Project Name"
                    className="flex-1 bg-gray-900 border border-gray-600 rounded p-2 text-white focus:border-cyan-500 focus:outline-none"
                />
                <button 
                    onClick={createProject}
                    className="bg-cyan-600 hover:bg-cyan-500 text-white font-bold py-2 px-4 rounded transition"
                >
                    Create
                </button>
            </div>

            {loading ? (
                <p className="text-gray-400">Loading projects...</p>
            ) : projects.length === 0 ? (
                <p className="text-gray-400">No projects found. Create one to start saving notebooks!</p>
            ) : (
                <div className="space-y-4">
                    {projects.map(p => (
                        <div key={p.id} className="p-4 bg-gray-900 border border-gray-700 rounded flex justify-between items-center hover:border-cyan-500 transition">
                            <div>
                                <h3 className="text-lg font-semibold text-white">{p.name}</h3>
                                <p className="text-sm text-gray-500">ID: {p.id} | Created: {new Date(p.created_at).toLocaleString()}</p>
                            </div>
                            <button className="bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded text-sm text-cyan-200">
                                Open Workspace
                            </button>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};
