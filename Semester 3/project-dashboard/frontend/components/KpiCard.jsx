// frontend/components/KpiCard.jsx
export default function KpiCard({ label, value }) {
  return (
    <div className="p-4 bg-white rounded-2xl shadow">
      <div className="text-sm text-gray-500">{label}</div>
      <div className="text-2xl font-semibold">{value}</div>
    </div>
  );
}
