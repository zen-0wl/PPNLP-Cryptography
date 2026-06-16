import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import QuantumThreat from "./pages/QuantumThreat";
import LWEDemo from "./pages/LWEDemo";
import Benchmarks from "./pages/Benchmarks";
import About from "./pages/About";
import ClassicalCrypto from "./pages/ClassicalCrypto";
import NoisePage from "./pages/NoisePage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quantum-threat" element={<QuantumThreat />} />
        <Route path="/lwe-demo" element={<LWEDemo />} />
        <Route path="/benchmarks" element={<Benchmarks />} />
        <Route path="/about" element={<About />} />

        <Route
        path="/classical-crypto"
        element={<ClassicalCrypto />}
      />
      <Route
        path="/noise"
        element={<NoisePage />}
      />
      </Routes>
    </BrowserRouter>
  );
}

export default App;