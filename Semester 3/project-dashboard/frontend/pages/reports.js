// frontend/pages/reports.js
import { useEffect, useState } from "react";

export default function ReportsPage() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    (async () => {
      try {
        const res = await fetch("http://localhost:3001/api/reports/summary");
        const json = await res.json();
        setData(json);
      } catch (e) {
        setData(null);
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  if (loading) return <p>Loading…</p>;
  if (!data) return <p>Could not load report.</p>;

  // …render your KPIs / chart / table here…
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Reports</h2>
      <pre className="text-sm bg-gray-50 p-3 rounded">{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
