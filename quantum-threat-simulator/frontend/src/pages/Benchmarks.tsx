export default function Benchmarks() {

  const benchmarkData = [
    {
      algorithm: "RSA-2048",
      keySize: "256 B",
      encrypt: "1.2 ms",
      decrypt: "1.0 ms",
    },
    {
      algorithm: "ECC-256",
      keySize: "32 B",
      encrypt: "0.9 ms",
      decrypt: "0.7 ms",
    },
    {
      algorithm: "LWE Demo",
      keySize: "4 KB",
      encrypt: "1.5 ms",
      decrypt: "1.4 ms",
    },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-5xl font-bold mb-4">
        Benchmarks & Security Analysis
      </h1>

      <p className="text-slate-400 mb-12">
        Comparing classical cryptography against
        post-quantum cryptography.
      </p>

      {/* Benchmark Table */}

      <div className="bg-slate-900 rounded-xl p-8 mb-12">

        <h2 className="text-3xl font-bold mb-6">
          Performance Benchmarks
        </h2>

        <table className="w-full">

          <thead>
            <tr className="text-left border-b border-slate-700">
              <th className="pb-4">Algorithm</th>
              <th className="pb-4">Key Size</th>
              <th className="pb-4">Encrypt</th>
              <th className="pb-4">Decrypt</th>
            </tr>
          </thead>

          <tbody>
            {benchmarkData.map((item) => (
              <tr
                key={item.algorithm}
                className="border-b border-slate-800"
              >
                <td className="py-4">
                  {item.algorithm}
                </td>

                <td>
                  {item.keySize}
                </td>

                <td>
                  {item.encrypt}
                </td>

                <td>
                  {item.decrypt}
                </td>
              </tr>
            ))}
          </tbody>

        </table>

      </div>

      {/* Security Comparison */}

      <div className="bg-slate-900 rounded-xl p-8 mb-12">

        <h2 className="text-3xl font-bold mb-6">
          Security Comparison
        </h2>

        <table className="w-full">

          <thead>
            <tr className="border-b border-slate-700">
              <th className="text-left pb-4">Property</th>

              <th className="text-center pb-4">
                RSA
              </th>

              <th className="text-center pb-4">
                ECC
              </th>

              <th className="text-center pb-4">
                LWE
              </th>
            </tr>
          </thead>

          <tbody>

            <tr>
              <td className="py-4">
                Quantum Resistant
              </td>

              <td className="text-center text-2xl">
                  ❌
                </td>

                <td className="text-center text-2xl">
                  ❌
                </td>

                <td className="text-center text-2xl">
                  ✅
                </td>
            </tr>

            <tr>
              <td className="py-4">
                Key Size
              </td>

              <td className="text-center">
                Small
              </td>

              <td className="text-center">
                Very Small
              </td>

              <td className="text-center">
                Large
              </td>
            </tr>

            <tr>
              <td className="py-4">
                Ciphertext Size
              </td>

              <td className="text-center">
                Small
              </td>

              <td className="text-center">
                Small
              </td>

              <td className="text-center">
                Large
              </td>
            </tr>

            <tr>
              <td className="py-4">
                Maturity
              </td>
              
              <td className="text-center">
                High
              </td>

              <td className="text-center">
                High
              </td>

              <td className="text-center">
                Growing
              </td>
            </tr>

          </tbody>

        </table>

      </div>

      {/* Tradeoffs */}

      <div className="grid md:grid-cols-3 gap-6">

        <div className="bg-slate-900 p-6 rounded-xl">
          <h3 className="text-2xl font-bold mb-4">
            RSA
          </h3>

          <p>✓ Mature</p>
          <p>✓ Small Keys</p>
          <p className="text-red-400">
            ✗ Quantum Vulnerable
          </p>
        </div>

        <div className="bg-slate-900 p-6 rounded-xl">
          <h3 className="text-2xl font-bold mb-4">
            ECC
          </h3>

          <p>✓ Efficient</p>
          <p>✓ Very Small Keys</p>
          <p className="text-red-400">
            ✗ Quantum Vulnerable
          </p>
        </div>

        <div className="bg-slate-900 p-6 rounded-xl">
          <h3 className="text-2xl font-bold mb-4">
            LWE
          </h3>

          <p className="text-emerald-400">
            ✓ Quantum Resistant
          </p>

          <p>✗ Larger Keys</p>
          <p>✗ Larger Ciphertexts</p>
        </div>

      </div>

    </div>
  );
}