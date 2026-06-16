import { motion } from "framer-motion";

export default function QuantumAttackFlow() {
  const steps = [
    "RSA Public Key",
    "Large Integer N = p × q",
    "Classical Computer\n~10¹⁸ years",
    "Quantum Computer\nShor's Algorithm",
    "Factors Found",
    "Private Key Recovered",
  ];

  return (
    <div className="max-w-3xl mx-auto">
  {steps.map((step, index) => (
    <div key={index} className="flex flex-col items-center">

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        viewport={{ once: true }}
        className="w-full rounded-xl border border-slate-700 bg-slate-900 p-6 text-center shadow-lg"
      >
        <p className="whitespace-pre-line text-lg font-medium">
          {step}
        </p>
      </motion.div>

      {index !== steps.length - 1 && (
        <div className="flex flex-col items-center py-4">
          <div className="h-8 w-px bg-indigo-500" />
          <div className="text-indigo-400 text-xl">▼</div>
        </div>
      )}
    </div>
  ))}
</div>
  );
}