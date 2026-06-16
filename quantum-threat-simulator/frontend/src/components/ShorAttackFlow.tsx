const steps = [
  "RSA Public Key",
  "N = p × q",
  "Quantum Computer",
  "Period Finding",
  "Factors Discovered",
  "Private Key Recovered"
];

export default function ShorAttackFlow() {
  return (
    <div className="max-w-3xl mx-auto">

      {steps.map((step, index) => (
        <div
          key={index}
          className="flex flex-col items-center"
        >
          <div className="w-full bg-slate-900 border border-slate-700 rounded-xl p-6 text-center">
            <h3 className="text-xl font-semibold">
              {step}
            </h3>
          </div>

          {index < steps.length - 1 && (
            <div className="py-4 text-indigo-400 text-3xl">
              ↓
            </div>
          )}
        </div>
      ))}

    </div>
  );
}