import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { noise: 1, success: 100 },
  { noise: 3, success: 100 },
  { noise: 7, success: 95 },
  { noise: 15, success: 40 },
];

export default function NoiseVisualisation() {
  return (
    <div className="space-y-10">

      <div className="grid md:grid-cols-4 gap-4">

        <div className="bg-slate-900 rounded-xl p-4 text-center">
          <h3 className="font-bold">Noise = 1</h3>
          <p className="text-emerald-400 text-2xl">✓</p>
        </div>

        <div className="bg-slate-900 rounded-xl p-4 text-center">
          <h3 className="font-bold">Noise = 3</h3>
          <p className="text-emerald-400 text-2xl">✓</p>
        </div>

        <div className="bg-slate-900 rounded-xl p-4 text-center">
          <h3 className="font-bold">Noise = 7</h3>
          <p className="text-emerald-400 text-2xl">✓</p>
        </div>

        <div className="bg-slate-900 rounded-xl p-4 text-center">
          <h3 className="font-bold">Noise = 15</h3>
          <p className="text-red-400 text-2xl">✗</p>
        </div>

      </div>

      <div className="bg-slate-900 rounded-xl p-6">

        <h3 className="text-xl font-bold mb-4">
          Noise vs Decryption Success Rate
        </h3>

        <div style={{ width: "100%", height: 350 }}>
          <ResponsiveContainer>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="noise" />

              <YAxis
                domain={[0, 100]}
              />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="success"
                strokeWidth={3}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

      </div>

    </div>
  );
}