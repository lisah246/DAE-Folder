// frontend/pages/_app.js
import "@/styles/globals.css";
import Navbar from "@/components/Navbar";   // <- only this import

export default function App({ Component, pageProps }) {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="mx-auto max-w-6xl px-4 py-6">
        <Component {...pageProps} />
      </main>
    </div>
  );
}
