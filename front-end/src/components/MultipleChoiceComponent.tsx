import type { Question, Option } from "../types/Types";
import { useSurveyContext } from "../context/SurveyContext";
import { useState } from "react";
import InputTextComponent from "./InputTextComponent";
interface Props {
  question: Question;
  questionId: number; // Optional prop to identify the question
  listId: number; // Optional prop to identify the list
}

const MultipleChoiceComponent = ({ question, listId, questionId }: Props) => {
  const { updateOptionPercent, addOption } = useSurveyContext();
  const [percents, setPercents] = useState<number[]>(() =>
    question.options.map((option) => option.percent || 0)
  );

  const validOptions = question.options.filter(
    (option) => option.label !== "__other_option__"
  );

  const otherOptions = question.options.filter(
    (option) => option.label === "__other_option__"
  );

  const handlePercentChange = (index: number, newPercent: number) => {
    setPercents((prev) =>
      prev.map((percent, i) => (i === index ? newPercent : percent))
    );
    updateOptionPercent(listId, questionId, index, newPercent);
  };

  const handleAddOption = () => {
    const option: Option = {
      label: "__other_option__",
      percent: 0,
      count: 0,
      xpath: ".//input[@type='text']",
      value: "",
    };
    addOption(listId, questionId, option);
  };

  return (
    <div>
      <h3>{question.heading}</h3>
      {validOptions.map((option, index) => (
        <div key={index}>
          <input type="radio" name={question.heading} value={option.label} />
          <label htmlFor={question.xpath}>
            {option.label !== "__other_option__" && (
              <>
                {option.label}
                <input
                  style={{ width: "50px" }}
                  type="number"
                  onChange={(e) =>
                    handlePercentChange(index, Number(e.target.value))
                  }
                  value={percents[index] || 0}
                  min={0}
                  max={100}
                />
              </>
            )}
          </label>
        </div>
      ))}

      {otherOptions.length > 0 && (
        <>
          <input
            type="radio"
            name={question.heading}
            value="__other_option__"
          />
          Other: _______________________
          <button onClick={handleAddOption}>+</button>
          <div>
            {otherOptions.map((option, index) => (
              <InputTextComponent
                key={index}
                listId={listId}
                questionId={questionId}
                optionId={validOptions.length + index}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default MultipleChoiceComponent;
