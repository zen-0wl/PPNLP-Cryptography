import { useEffect, useState } from "react";
import { api } from "../services/api";

export default function BackendStatus() {
  const [status, setStatus] = useState("");

  useEffect(() => {
    api.get("/lwe/status").then((res) => {
      setStatus(res.data.algorithm);
    });
  }, []);

  return (
    <div className="rounded-xl bg-slate-900 p-6">
      <h3 className="font-bold">
        Backend Connection
      </h3>

      <p className="mt-2 text-emerald-400">
        {status}
      </p>
    </div>
  );
}