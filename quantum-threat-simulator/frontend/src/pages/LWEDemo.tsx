import { useState } from "react";
import { api } from "../services/api";

export default function LWEDemo() {

  const [keyData, setKeyData] = useState<any>(null);

  const [message, setMessage] = useState(1);

  const [ciphertext, setCiphertext] = useState<number | null>(null);

  const [decrypted, setDecrypted] = useState<number | null>(null);

  async function generateKeys() {

    const res = await api.get("/lwe/keygen");

    setKeyData(res.data);
  }

  async function encryptMessage() {

    const res = await api.post("/lwe/encrypt", {
      message
    });

    setCiphertext(res.data.ciphertext);
  }

  async function decryptMessage() {

    if (ciphertext === null) return;

    const res = await api.post("/lwe/decrypt", {
      ciphertext
    });

    setDecrypted(res.data.message);
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-5xl font-bold mb-10">
        LWE Demonstration
      </h1>

      <button
        onClick={generateKeys}
        className="px-6 py-3 bg-indigo-600 rounded-lg"
      >
        Generate Key Pair
      </button>

      {keyData && (
        <div className="mt-8 space-y-6">

          <div className="bg-slate-900 p-6 rounded-xl">
            <h2 className="font-bold mb-2">
              Matrix A
            </h2>

            <pre>
              {JSON.stringify(keyData.A, null, 2)}
            </pre>
          </div>

          <div className="bg-slate-900 p-6 rounded-xl">
            <h2 className="font-bold mb-2">
              Secret Vector s
            </h2>

            <pre>
              {JSON.stringify(keyData.s)}
            </pre>
          </div>

          <div className="bg-slate-900 p-6 rounded-xl">
            <h2 className="font-bold mb-2">
              Public Vector b
            </h2>

            <pre>
              {JSON.stringify(keyData.b)}
            </pre>
          </div>

        </div>
      )}

      <div className="mt-12">

        <h2 className="text-2xl font-bold mb-4">
          Encryption Demo
        </h2>

        <input
          type="number"
          value={message}
          onChange={(e) => setMessage(Number(e.target.value))}
          className="text-black p-2 rounded"
        />

        <button
          onClick={encryptMessage}
          className="ml-4 px-4 py-2 bg-emerald-600 rounded"
        >
          Encrypt
        </button>

        {ciphertext !== null && (
          <div className="mt-4">
            Ciphertext: {ciphertext}
          </div>
        )}

        <button
          onClick={decryptMessage}
          className="mt-4 px-4 py-2 bg-orange-600 rounded block"
        >
          Decrypt
        </button>

        {decrypted !== null && (
          <div className="mt-4 text-emerald-400">
            Recovered Message: {decrypted}
          </div>
        )}

      </div>

    </div>
  );
}