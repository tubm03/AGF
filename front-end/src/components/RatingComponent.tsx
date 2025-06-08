import type { Question } from "../types/Types";
import { useSurveyContext } from "../context/SurveyContext";
import { useState } from "react";

interface Props {
  question: Question;
  questionId: number; // Optional prop to identify the question
  listId: number; // Optional prop to identify the list
}

const RatingComponent = ({ question, listId, questionId }: Props) => {
  const { updateOptionPercent } = useSurveyContext();
  const [percents, setPercents] = useState<number[]>(() =>
    question.options.map((option) => option.percent || 0)
  );

  const handlePercentChange = (index: number, newPercent: number) => {
    setPercents((prev) =>
      prev.map((percent, i) => (i === index ? newPercent : percent))
    );
    updateOptionPercent(listId, questionId, index, newPercent);
  };
  return (
    <div>
      <h3>{question.heading}</h3>
      {question.options.map((option, index) => (
        <div>
          {option.label}
          <input
            style={{ width: "50px" }}
            type="number"
            value={percents[index]}
            min={0}
            max={100}
            onChange={(e) => {
              handlePercentChange(index, Number(e.target.value));
            }}
          />
        </div>
      ))}
    </div>
  );
};

export default RatingComponent;
