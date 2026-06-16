import { Link } from "react-router-dom";
import QuantumAttackFlow from "../components/QuantumAttackFlow";
import BackendStatus from "../components/BackendStatus";

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <nav className="border-b border-slate-800">
        <div className="mx-auto max-w-7xl px-6 py-4 flex justify-between items-center">
          <h1 className="text-xl font-bold">
            Quantum Threat Simulator
          </h1>

          <div className="flex gap-6 text-slate-300">
            <Link to="/classical-crypto">Classical Crypto</Link>
            <Link to="/quantum-threat">Quantum Threat</Link>
            <Link to="/lwe-demo">LWE Demo</Link>
            <Link to="/noise">Noise</Link>
            <Link to="/benchmarks">Benchmarks</Link>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="max-w-6xl mx-auto px-6 py-32 text-center">
        <span className="px-4 py-2 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20">
          Post-Quantum Cryptography
        </span>

        <h1 className="mt-8 text-7xl font-bold">
          Why RSA & ECC
          <br />
          Fail Against Quantum Computers
        </h1>

        <p className="mt-8 text-xl text-slate-400 max-w-3xl mx-auto">
          An interactive educational platform demonstrating how
          quantum computers threaten classical cryptography and
          why lattice-based encryption is considered a leading
          post-quantum solution.
        </p>

        <div className="mt-12 flex justify-center gap-4">
          <Link
            to="/quantum-threat"
            className="px-6 py-3 rounded-lg bg-indigo-600 hover:bg-indigo-500 transition"
          >
            Explore Quantum Threat
          </Link>

          <Link
            to="/lwe-demo"
            className="px-6 py-3 rounded-lg border border-slate-700 hover:bg-slate-900 transition"
          >
            Run LWE Demo
          </Link>
        </div>
      </section>

      {/* Security Comparison Cards */}
      <section className="max-w-6xl mx-auto px-6 pb-24">
        <div className="grid md:grid-cols-3 gap-6">

          <div className="rounded-2xl border border-red-500/20 bg-slate-900 p-6">
            <h3 className="text-2xl font-bold">RSA</h3>

            <div className="mt-4 inline-block rounded-full px-3 py-1 text-red-400 bg-red-500/10">
              Vulnerable
            </div>

            <p className="mt-4 text-slate-400">
              Security relies on integer factorization.
              Shor's algorithm can break RSA efficiently on a
              sufficiently powerful quantum computer.
            </p>
          </div>

          <div className="rounded-2xl border border-red-500/20 bg-slate-900 p-6">
            <h3 className="text-2xl font-bold">ECC</h3>

            <div className="mt-4 inline-block rounded-full px-3 py-1 text-red-400 bg-red-500/10">
              Vulnerable
            </div>

            <p className="mt-4 text-slate-400">
              Based on elliptic curve discrete logarithms.
              Also vulnerable to Shor's algorithm.
            </p>
          </div>

          <div className="rounded-2xl border border-emerald-500/20 bg-slate-900 p-6">
            <h3 className="text-2xl font-bold">LWE</h3>

            <div className="mt-4 inline-block rounded-full px-3 py-1 text-emerald-400 bg-emerald-500/10">
              Quantum Resistant
            </div>

            <p className="mt-4 text-slate-400">
              Based on lattice problems believed to remain
              difficult even for quantum computers.
            </p>
          </div>

        </div>
      </section>

      {/* Quantum Threat Section */}
      <section className="max-w-5xl mx-auto px-6 py-24">
        <h2 className="text-4xl font-bold text-center">
          The Quantum Threat
        </h2>

        <p className="mt-8 text-center text-slate-400 text-lg">
          Modern cryptography secures banking, messaging,
          e-commerce, software updates and digital identity.
          Quantum computers threaten many of today's most
          widely used cryptographic systems.
        </p>

        <div className="mt-12 grid md:grid-cols-2 gap-8">
          <div className="rounded-xl bg-slate-900 p-6">
            <h3 className="text-xl font-semibold">
              Classical Security
            </h3>

            <p className="mt-3 text-slate-400">
              RSA and ECC depend on mathematical problems
              that are computationally infeasible for
              classical computers.
            </p>
          </div>

          <div className="rounded-xl bg-slate-900 p-6">
            <h3 className="text-xl font-semibold">
              Quantum Computing
            </h3>

            <p className="mt-3 text-slate-400">
              Shor's algorithm changes the landscape by
              solving these problems dramatically faster,
              threatening current public-key cryptography.
            </p>
          </div>
        </div>
      </section>

      <section className="max-w-6xl mx-auto px-6 py-24">
      <h2 className="text-4xl font-bold text-center mb-12">
        How Quantum Computers Break RSA
      </h2>

      <QuantumAttackFlow />
    </section>

    <section className="max-w-6xl mx-auto px-6 py-24">
      <h2 className="text-4xl font-bold text-center mb-8">
        Backend Integration
      </h2>

      <BackendStatus />
    </section>
    </div>
  );
}