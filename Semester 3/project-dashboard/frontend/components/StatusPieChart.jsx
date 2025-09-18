// frontend/components/StatusPieChart.jsx
import { Doughnut } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
ChartJS.register(ArcElement, Tooltip, Legend);

export default function StatusPieChart({ statusCounts }) {
  // statusCounts is an object like: { todo: 3, "in_progress": 4, done: 2 }
  const labels = ["todo", "in_progress", "done"];
  const values = labels.map((key) => statusCounts[key] || 0);

  const data = {
    labels,
    datasets: [
      {
        label: "Tasks",
        data: values,
      },
    ],
  };

  return (
    <div className="p-4 bg-white rounded-2xl shadow">
      <h3 className="font-semibold mb-3">Task Status</h3>
      <Doughnut data={data} />
    </div>
  );
}
