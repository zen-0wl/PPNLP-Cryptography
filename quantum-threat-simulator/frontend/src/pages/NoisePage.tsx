import NoiseVisualisation from "../components/NoiseGraph";

export default function NoisePage() {
  return (
    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-5xl font-bold mb-10">
        LWE Noise Visualisation
      </h1>

      <p className="text-slate-400 mb-12 max-w-3xl">
        Learning With Errors (LWE) relies on adding small
        amounts of noise to hide the secret key.
        Small noise preserves correct decryption,
        while excessive noise eventually causes failures.
      </p>

      <NoiseVisualisation />

    </div>
  );
}