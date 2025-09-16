import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export async function getServerSideProps() {
  let projects = [];
  let error = null;

  try {
    const res = await fetch("http://localhost:3001/api/projects");
    if (res.ok) {
      projects = await res.json();
    } else {
      error = `Backend responded ${res.status}`;
    }
  } catch (e) {
    error = "Backend not reachable";
  }

  return { props: { projects, error } };
}

export default function Home({ projects, error }) {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-1 p-4">
        <h2 className="text-xl font-semibold mb-3">Projects</h2>

        {error && (
          <div className="mb-3 rounded border border-red-300 bg-red-50 p-3 text-sm">
            {error}. Is the backend running on <code>http://localhost:3001</code>?
          </div>
        )}

        {projects.length === 0 ? (
          <p className="text-slate-600">No projects to show.</p>
        ) : (
          <ul className="space-y-2">
            {projects.map((p) => (
              <li key={p.id} className="border rounded p-3">
                <div className="font-medium">{p.name}</div>
                {p.dueDate && (
                  <div className="text-xs text-slate-500">Due: {p.dueDate}</div>
                )}
              </li>
            ))}
          </ul>
        )}
      </main>
      <Footer />
    </div>
  );
}
