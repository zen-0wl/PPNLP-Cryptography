import QuantumComparison from "../components/QuantumComparison";
import ShorAttackFlow from "../components/ShorAttackFlow";

export default function QuantumThreat() {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-5xl font-bold text-center mb-16">
        Why RSA & ECC Break Under Quantum Computing
      </h1>

      <section className="max-w-6xl mx-auto">
        <QuantumComparison />
      </section>

      <section className="max-w-4xl mx-auto mt-24">
        <h2 className="text-3xl font-bold text-center mb-12">
          How Shor's Algorithm Breaks RSA
        </h2>

        <ShorAttackFlow />
      </section>

      <section className="max-w-4xl mx-auto mt-16">
        <div className="bg-slate-900 rounded-2xl p-8">
          <h3 className="text-2xl font-bold mb-4">
            Why This Matters
          </h3>

          <p className="text-slate-300">
            RSA security depends on the difficulty of
            factoring very large integers. Classical
            computers would require impractical amounts
            of time, while quantum computers running
            Shor's Algorithm can theoretically perform
            this task efficiently and recover private
            keys.
          </p>
        </div>
      </section>

    </div>
  );
}