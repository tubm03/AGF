// components/SurveyForm.tsx
import { useNavigate } from "react-router-dom";
import ListQuestions from "./ListQuestions";
import { useSurveyContext } from "../context/SurveyContext";
import React, { useState } from "react";
import { API_URL } from "../../config/setting";
import axios from "axios";

const SurveyForm: React.FC = () => {
  const navigate = useNavigate();

  // ✅ Sử dụng context thay vì local state
  const { formData } = useSurveyContext();
  const [numberOfFill, setNumberOfFill] = useState<number>(0);

  const autoFill = async () => {
    try {
      await axios.post(`${API_URL}/autofill`, {
        formData: formData,
        numberOfFill: numberOfFill,
      });
    } catch (error) {
      console.error("Auto fill request failed:", error);
      alert("Auto fill failed. Please try again.");
    }
  };

  // ✅ Set data từ location state vào context
  // useEffect(() => {
  //   const stateData = location.state?.data;
  //   if (stateData && !formData) {
  //     setFormData(stateData as Form);
  //   }
  // }, [location.state, formData, setFormData]);

  if (!formData) {
    return (
      <div>
        <h2>No Survey Data Found</h2>
        <p>Please start from the home page.</p>
        <button onClick={() => navigate("/")}>Go to Home</button>
      </div>
    );
  }

  return (
    <div>
      <h1>Page</h1>
      {formData.lists.map((list, index) => (
        <div key={index}>
          <h2>List question of page {index + 1}</h2>
          <ListQuestions list={list} listId={index} />
        </div>
      ))}
      <div>
        <input
          type="number"
          value={numberOfFill}
          onChange={(e) => setNumberOfFill(Number(e.target.value))}
        ></input>
      </div>

      <button
        onClick={() => {
          console.log("Final form data:", formData);
          alert("Survey submitted!");
          autoFill();
        }}
      >
        Submit Survey
      </button>
    </div>
  );
};

export default SurveyForm;
