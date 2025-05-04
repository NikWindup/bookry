import Landing from "./pages/Landing"
import { Routes, Route} from "react-router-dom"
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";


function App() {
  return (
      <Routes>
        <Route path="/landing" element={Landing()} ></Route>
      <Route path="/login" element={Login()} ></Route>
      <Route path="/register" element={Register()} ></Route>
      <Route path="/dashboard" element={Dashboard()} ></Route>
      </Routes>
  );
}

export default App