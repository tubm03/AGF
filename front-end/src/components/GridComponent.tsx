import type { Question } from "../types/Types";
import { useSurveyContext } from "../context/SurveyContext";
import { useState } from "react";
import "../styles/styles.css"; // Ensure styles are imported

interface Props {
  question: Question;
  listId: number;
  questionId: number;
  inputType: "checkbox" | "radio";
}

const GridComponent = ({ question, listId, questionId, inputType }: Props) => {
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
    <div className="grid-container">
      <h3>{question.heading}</h3>

      <div
        className="grid-table"
        style={{
          gridTemplateColumns: `120px repeat(${question.columns.length}, 1fr)`,
        }}
      >
        <div></div>
        {question.columns.map((col, colIndex) => (
          <div key={colIndex} className="grid-header">
            {col}
          </div>
        ))}

        {question.rows.map((row, rowIndex) => (
          <>
            <div key={`row-${rowIndex}`} className="row-header">
              {row}
            </div>

            {question.columns.map((col, colIndex) => (
              <div key={`${rowIndex}-${colIndex}`} className="grid-cell">
                <input
                  type={inputType}
                  name={`${question.xpath}-${rowIndex}`}
                  value={col}
                  className="grid-input"
                />
                <input
                  type="number"
                  className="grid-percent-input"
                  min={0}
                  max={100}
                  value={
                    percents[rowIndex * question.columns.length + colIndex]
                  }
                  onChange={(e) => {
                    const newPercent = Number(e.target.value);
                    handlePercentChange(
                      rowIndex * question.columns.length + colIndex,
                      newPercent
                    );
                  }}
                />
              </div>
            ))}
          </>
        ))}
      </div>
    </div>
  );
};

export default GridComponent;
