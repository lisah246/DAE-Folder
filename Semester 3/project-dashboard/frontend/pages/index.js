// frontend/pages/index.js
export async function getServerSideProps() {
  try {
    const res = await fetch("http://localhost:3001/api/projects");
    const projects = res.ok ? await res.json() : [];
    return { props: { projects, error: res.ok ? null : "Backend error" } };
  } catch {
    return { props: { projects: [], error: "Backend not reachable" } };
  }
}

export default function Home({ projects, error }) {
  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Projects</h2>

      {error && (
        <p className="mb-3 text-red-600">
          {error}. Is the backend running on <code>http://localhost:3001</code>?
        </p>
      )}

      <ul className="divide-y">
        {projects.map((p) => (
          <li key={p.id} className="py-2">
            <div className="font-medium">{p.name}</div>
            {p.dueDate && (
              <div className="text-sm text-gray-600">
                Due: {p.dueDate}
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
