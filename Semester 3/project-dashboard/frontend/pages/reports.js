// frontend/pages/reports.js
import { useEffect, useState } from "react";

export default function ReportsPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    (async () => {
      try {
        const res = await fetch("http://localhost:3001/api/reports/summary");
        
        if (!res.ok) {
          throw new Error(`HTTP ${res.status}: ${res.statusText}`);
        }
        
        const json = await res.json();
        
        // Add sample tasks if none exist (for portfolio demo)
        if (json.totals.tasks === 0) {
          json.totals.tasks = 24;
          json.statusBreakdown = [
            { status: 'completed', count: 12 },
            { status: 'in-progress', count: 8 },
            { status: 'todo', count: 4 }
          ];
          json.overdue = [
            { id: 1, title: 'Update client presentation', dueDate: '2025-09-20' },
            { id: 2, title: 'Code review for authentication', dueDate: '2025-09-21' }
          ];
          json.upcoming = [
            { id: 3, title: 'Deploy staging environment', dueDate: '2025-09-25' },
            { id: 4, title: 'Client feedback session', dueDate: '2025-09-26' },
            { id: 5, title: 'Database optimization', dueDate: '2025-09-27' }
          ];
          // Add completion percentages
          json.completion = json.completion.map((project, index) => ({
            ...project,
            completionPct: [85, 72, 45, 90, 60, 35, 95, 20, 10][index] || 0
          }));
        }
        
        setData(json);
        setError(null);
      } catch (e) {
        console.error("Reports fetch error:", e);
        setError(e.message);
        setData(null);
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  if (loading) return <div className="p-6 text-center text-blue-600 text-xl">Loading dashboard...</div>;
  if (error) return <div className="p-6 text-center text-red-600 text-xl">Error: {error}</div>;
  if (!data) return <div className="p-6 text-center text-gray-600 text-xl">No data available.</div>;

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      {/* Header */}
      <div className="mb-8 text-center">
        <h2 className="text-4xl font-bold text-purple-600 mb-2">Project Dashboard</h2>
        <p className="text-gray-600">Real-time project analytics and insights</p>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {/* Clients Card */}
        <div className="bg-blue-500 text-white rounded-lg p-6 shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-blue-100 text-sm font-medium uppercase">Total Clients</p>
              <p className="text-4xl font-bold">{data.totals.clients}</p>
              <p className="text-blue-200 text-sm">+2 this month</p>
            </div>
            <div className="text-6xl opacity-20">👥</div>
          </div>
        </div>

        {/* Projects Card */}
        <div className="bg-green-500 text-white rounded-lg p-6 shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-green-100 text-sm font-medium uppercase">Active Projects</p>
              <p className="text-4xl font-bold">{data.totals.projects}</p>
              <p className="text-green-200 text-sm">87% completion rate</p>
            </div>
            <div className="text-6xl opacity-20">📊</div>
          </div>
        </div>

        {/* Tasks Card */}
        <div className="bg-purple-500 text-white rounded-lg p-6 shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-purple-100 text-sm font-medium uppercase">Total Tasks</p>
              <p className="text-4xl font-bold">{data.totals.tasks}</p>
              <p className="text-purple-200 text-sm">12 completed today</p>
            </div>
            <div className="text-6xl opacity-20">✅</div>
          </div>
        </div>
      </div>

      {/* Project Completion */}
      <div className="bg-white rounded-lg p-6 shadow-lg mb-8">
        <h3 className="text-2xl font-bold text-gray-800 mb-6">Project Completion Status</h3>
        
        {data.completion && data.completion.length > 0 ? (
          <div className="space-y-4">
            {data.completion.map((project, index) => {
              const colors = ['bg-blue-500', 'bg-green-500', 'bg-purple-500', 'bg-yellow-500', 'bg-red-500', 'bg-indigo-500', 'bg-pink-500', 'bg-teal-500', 'bg-orange-500'];
              return (
                <div key={project.id} className="border-l-4 border-gray-300 pl-4">
                  <div className="flex justify-between items-center mb-2">
                    <span className="font-semibold text-gray-800">{project.name}</span>
                    <span className="text-purple-600 font-bold">{project.completionPct || 0}%</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-3">
                    <div
                      className={`${colors[index % colors.length]} h-3 rounded-full transition-all duration-1000`}
                      style={{ width: `${project.completionPct || 0}%` }}
                    ></div>
                  </div>
                </div>
              );
            })}
          </div>
        ) : (
          <div className="text-center py-8 text-gray-500">No project data available</div>
        )}
      </div>

      {/* Task Status */}
      {data.statusBreakdown && data.statusBreakdown.length > 0 && (
        <div className="bg-white rounded-lg p-6 shadow-lg mb-8">
          <h3 className="text-2xl font-bold text-gray-800 mb-6">Task Status Distribution</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {data.statusBreakdown.map((status, index) => {
              const colors = ['bg-green-400', 'bg-blue-400', 'bg-yellow-400'];
              const textColors = ['text-green-800', 'text-blue-800', 'text-yellow-800'];
              return (
                <div key={status.status} className={`${colors[index]} text-white rounded-lg p-6 text-center shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300`}>
                  <p className="text-3xl font-bold mb-2">{status.count}</p>
                  <p className="font-medium capitalize text-lg">{status.status.replace('-', ' ')}</p>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Alerts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        {/* Overdue Tasks */}
        <div className="bg-red-50 border-2 border-red-200 rounded-lg p-6 shadow-lg">
          <div className="flex items-center mb-4">
            <div className="text-2xl mr-3">⚠️</div>
            <h3 className="text-xl font-bold text-red-800">Overdue Tasks</h3>
          </div>
          {data.overdue && data.overdue.length > 0 ? (
            <div className="space-y-3">
              {data.overdue.slice(0, 5).map((task) => (
                <div key={task.id} className="bg-white rounded-lg p-4 border border-red-200 hover:shadow-md transition-shadow">
                  <div className="font-semibold text-red-900">{task.title}</div>
                  <div className="text-red-700 text-sm">Due: {new Date(task.dueDate).toLocaleDateString()}</div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-4">
              <div className="text-4xl mb-2">🎉</div>
              <div className="text-red-700 font-medium">No overdue tasks!</div>
            </div>
          )}
        </div>

        {/* Upcoming Tasks */}
        <div className="bg-yellow-50 border-2 border-yellow-200 rounded-lg p-6 shadow-lg">
          <div className="flex items-center mb-4">
            <div className="text-2xl mr-3">📅</div>
            <h3 className="text-xl font-bold text-yellow-800">Upcoming Tasks</h3>
          </div>
          {data.upcoming && data.upcoming.length > 0 ? (
            <div className="space-y-3">
              {data.upcoming.slice(0, 5).map((task) => (
                <div key={task.id} className="bg-white rounded-lg p-4 border border-yellow-200 hover:shadow-md transition-shadow">
                  <div className="font-semibold text-yellow-900">{task.title}</div>
                  <div className="text-yellow-700 text-sm">Due: {new Date(task.dueDate).toLocaleDateString()}</div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-4 text-yellow-700">
              <div className="text-2xl mb-2">📋</div>
              <div className="font-medium">No upcoming tasks</div>
            </div>
          )}
        </div>
      </div>

      {/* Debug Section */}
      <details className="bg-white rounded-lg p-4 shadow-lg">
        <summary className="text-sm font-medium text-gray-700 cursor-pointer hover:text-purple-600">Raw Data (Debug)</summary>
        <pre className="text-xs bg-gray-100 p-4 rounded mt-4 overflow-auto max-h-64">
          {JSON.stringify(data, null, 2)}
        </pre>
      </details>
    </div>
  );
}