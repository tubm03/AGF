import { useSurveyContext } from "../context/SurveyContext";
import type { Question } from "../types/Types";
import InputDateComponent from "./InputDateComponent";

interface Props {
  questionId: number; // Optional prop to identify the question
  listId: number; // Optional prop to identify the list
  question: Question;
}

const DateComponent = ({ listId, questionId, question }: Props) => {
  const { addOption } = useSurveyContext();

  const handleAddOption = () => {
    const option = {
      label: "input date",
      percent: 0,
      count: 0,
      xpath: ".//input[@type='date']",
      value: "",
    };
    addOption(listId, questionId, option);
  };

  if (question.options.length === 0) {
    console.log("No options found, adding default option");
    handleAddOption();
  }

  return (
    <>
      <h3>{question.heading}</h3> <button onClick={handleAddOption}>+</button>
      <div>
        {question.options.map((option, index) => (
          <InputDateComponent
            listId={listId}
            questionId={questionId}
            optionId={index}
            option={option}
          ></InputDateComponent>
        ))}
      </div>
    </>
  );
};

export default DateComponent;
