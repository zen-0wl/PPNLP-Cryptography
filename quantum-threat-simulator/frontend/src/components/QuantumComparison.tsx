export default function QuantumComparison() {
  return (
    <div className="grid md:grid-cols-2 gap-8">

      <div className="bg-slate-900 rounded-2xl p-8 border border-slate-700">
        <h3 className="text-2xl font-bold mb-4">
          Classical Computer
        </h3>

        <div className="text-5xl mb-4">
          🖥️
        </div>

        <p className="text-slate-300">
          Attack Method:
        </p>

        <p className="font-semibold">
          Integer Factorization
        </p>

        <div className="mt-6 p-4 bg-slate-800 rounded-lg">
          <p className="text-slate-400">
            Estimated Time
          </p>

          <p className="text-3xl font-bold text-emerald-400">
            10¹⁸ Years
          </p>
        </div>
      </div>

      <div className="bg-slate-900 rounded-2xl p-8 border border-red-500/30">
        <h3 className="text-2xl font-bold mb-4">
          Quantum Computer
        </h3>

        <div className="text-5xl mb-4">
          ⚛️
        </div>

        <p className="text-slate-300">
          Attack Method:
        </p>

        <p className="font-semibold">
          Shor's Algorithm
        </p>

        <div className="mt-6 p-4 bg-slate-800 rounded-lg">
          <p className="text-slate-400">
            Complexity
          </p>

          <p className="text-3xl font-bold text-red-400">
            Polynomial Time
          </p>
        </div>
      </div>

    </div>
  );
}