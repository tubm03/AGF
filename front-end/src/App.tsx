import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import SurveyForm from "./components/SurveyForm";
import { SurveyProvider } from "./context/SurveyContext";

function App() {
  return (
    <SurveyProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/survey" element={<SurveyForm />} />
          <Route path="*" element={<div>404 Not Found</div>} />
        </Routes>
      </Router>
    </SurveyProvider>
  );
}

export default App;
