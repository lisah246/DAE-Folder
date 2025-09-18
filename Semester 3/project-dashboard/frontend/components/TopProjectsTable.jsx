// frontend/components/TopProjectsTable.jsx
export default function TopProjectsTable({ projects }) {
  // projects is [{ id, name, completionPct }, ...]
  const rows = (projects || [])
    .filter(p => p.completionPct !== null && p.completionPct !== undefined)
    .sort((a, b) => (b.completionPct ?? 0) - (a.completionPct ?? 0))
    .slice(0, 5);

  return (
    <div className="p-4 bg-white rounded-2xl shadow overflow-x-auto">
      <h3 className="font-semibold mb-3">Top 5 Projects by Completion</h3>
      <table className="w-full text-sm">
        <thead className="text-left border-b">
          <tr>
            <th className="py-2 pr-4">Project</th>
            <th className="py-2">Completion %</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((p) => (
            <tr key={p.id} className="border-b last:border-0">
              <td className="py-2 pr-4">{p.name}</td>
              <td className="py-2">{p.completionPct?.toFixed(0) ?? "—"}</td>
            </tr>
          ))}
          {rows.length === 0 && (
            <tr>
              <td colSpan={2} className="py-3 text-gray-500">
                No completion data yet.
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
