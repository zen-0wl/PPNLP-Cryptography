import { useState } from "react";
import { api } from "../services/api";

export default function ClassicalCrypto() {

  const [rsaKeys, setRSAKeys] = useState<any>(null);

  const [message, setMessage] = useState(42);

  const [ciphertext, setCiphertext] = useState<number | null>(null);

  const [decrypted, setDecrypted] = useState<number | null>(null);

  const [eccData, setECCData] = useState<any>(null);

  async function generateRSA() {
    const res = await api.get("/classical/rsa/keygen");

    setRSAKeys(res.data);
  }

  async function encryptRSA() {

    const res = await api.post(
      "/classical/rsa/encrypt",
      {
        value: message
      }
    );

    setCiphertext(
      res.data.ciphertext
    );
  }

  async function decryptRSA() {

    if (ciphertext === null) return;

    const res = await api.post(
      "/classical/rsa/decrypt",
      {
        value: ciphertext
      }
    );

    setDecrypted(
      res.data.message
    );
  }

  async function runECC() {

    const res = await api.get(
      "/classical/ecc/exchange"
    );

    setECCData(
      res.data
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-5xl font-bold mb-12">
        Classical Cryptography
      </h1>

      {/* RSA */}

      <div className="bg-slate-900 p-8 rounded-xl mb-10">

        <h2 className="text-3xl font-bold mb-4">
          RSA Demonstration
        </h2>

        <button
          onClick={generateRSA}
          className="bg-indigo-600 px-4 py-2 rounded"
        >
          Generate Keys
        </button>

        {rsaKeys && (
          <div className="mt-4">
            <p>
              Public Key:
              {" "}
              {JSON.stringify(rsaKeys.public_key)}
            </p>

            <p>
              Private Key:
              {" "}
              {JSON.stringify(rsaKeys.private_key)}
            </p>
          </div>
        )}

        <div className="mt-6">

          <input
            type="number"
            value={message}
            onChange={(e) =>
              setMessage(Number(e.target.value))
            }
            className="text-black p-2 rounded"
          />

          <button
            onClick={encryptRSA}
            className="ml-4 bg-emerald-600 px-4 py-2 rounded"
          >
            Encrypt
          </button>

          <button
            onClick={decryptRSA}
            className="ml-4 bg-orange-600 px-4 py-2 rounded"
          >
            Decrypt
          </button>

          {ciphertext !== null && (
            <p className="mt-4">
              Ciphertext: {ciphertext}
            </p>
          )}

          {decrypted !== null && (
            <p className="mt-2 text-emerald-400">
              Recovered Message:
              {" "}
              {decrypted}
            </p>
          )}

        </div>

      </div>

      {/* ECC */}

      <div className="bg-slate-900 p-8 rounded-xl">

        <h2 className="text-3xl font-bold mb-4">
          ECC Key Exchange
        </h2>

        <button
          onClick={runECC}
          className="bg-indigo-600 px-4 py-2 rounded"
        >
          Run Exchange
        </button>

        {eccData && (
          <div className="mt-6">

            <p>
              Alice Public Key:
              {" "}
              {eccData.alice_public}
            </p>

            <p>
              Bob Public Key:
              {" "}
              {eccData.bob_public}
            </p>

            <p className="text-emerald-400">
              Shared Secret:
              {" "}
              {eccData.shared_secret}
            </p>

          </div>
        )}

      </div>

    </div>
  );
}