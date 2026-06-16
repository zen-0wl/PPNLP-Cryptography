import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import QuantumThreat from "./pages/QuantumThreat";
import LWEDemo from "./pages/LWEDemo";
import Benchmarks from "./pages/Benchmarks";
import About from "./pages/About";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quantum-threat" element={<QuantumThreat />} />
        <Route path="/lwe-demo" element={<LWEDemo />} />
        <Route path="/benchmarks" element={<Benchmarks />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;