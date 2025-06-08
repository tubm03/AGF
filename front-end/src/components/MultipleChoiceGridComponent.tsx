import type { Question } from "../types/Types";
import { useSurveyContext } from "../context/SurveyContext";
import { useState } from "react";

interface Props {
  question: Question;
  listId: number; // Optional prop to identify the list
  questionId: number; // Optional prop to identify the question
}

const MultipleChoiceGridComponent = ({
  question,
  listId,
  questionId,
}: Props) => {
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
    <div style={{ margin: "20px 0" }}>
      <h3>{question.heading}</h3>

      {/* Grid Container */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `200px repeat(${question.columns.length}, 1fr)`,
          gap: "10px",
          border: "1px solid #ddd",
          borderRadius: "8px",
          padding: "15px",
          backgroundColor: "#fafafa",
        }}
      >
        {/* Header Row - Empty cell + Column Headers */}
        <div></div> {/* Empty cell for top-left corner */}
        {question.columns.map((col, colIndex) => (
          <div
            key={colIndex}
            style={{
              fontWeight: "bold",
              textAlign: "center",
              padding: "10px",
              backgroundColor: "#e9ecef",
              borderRadius: "4px",
              fontSize: "14px",
            }}
          >
            {col}
          </div>
        ))}
        {/* Data Rows */}
        {question.rows.map((row, rowIndex) => (
          <>
            {/* Row Header */}
            <div
              key={`row-${rowIndex}`}
              style={{
                fontWeight: "bold",
                padding: "10px",
                backgroundColor: "#e9ecef",
                borderRadius: "4px",
                display: "flex",
                alignItems: "center",
                fontSize: "14px",
              }}
            >
              {row}
            </div>

            {/* Radio buttons for each column in this row */}
            {question.columns.map((col, colIndex) => (
              <div
                key={`${rowIndex}-${colIndex}`}
                style={{
                  display: "inline-block",
                  justifyContent: "center",
                  alignItems: "center",
                  padding: "10px",
                  backgroundColor: "white",
                  borderRadius: "4px",
                  border: "1px solid #e9ecef",
                }}
              >
                <input
                  type="radio"
                  name={`${question.xpath}-${rowIndex}`}
                  value={col}
                  style={{
                    transform: "scale(1.2)",
                    cursor: "pointer",
                  }}
                />
                <input
                  type="number"
                  style={{ width: "50px" }}
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
                ></input>
              </div>
            ))}
          </>
        ))}
      </div>
    </div>
  );
};

export default MultipleChoiceGridComponent;
