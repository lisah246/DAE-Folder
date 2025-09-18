// frontend/components/Navbar.jsx
import Link from "next/link";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur shadow-sm">
      <div className="mx-auto max-w-6xl px-4 py-3 flex items-center justify-between">
        <h1 className="text-lg font-semibold">Project Dashboard</h1>
        <nav className="flex gap-6 text-sm">
          <Link href="/" className="hover:text-blue-600">Home</Link>
          <Link href="/reports" className="hover:text-blue-600">Reports</Link>
        </nav>
      </div>
    </header>
  );
}
