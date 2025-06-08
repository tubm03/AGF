// MultipleChoiceGridComponent.tsx
import type { Question } from "../types/Types";
import GridComponent from "./GridComponent";

interface Props {
  question: Question;
  listId: number;
  questionId: number;
}

const MultipleChoiceGridComponent = ({
  question,
  listId,
  questionId,
}: Props) => {
  return (
    <GridComponent
      question={question}
      listId={listId}
      questionId={questionId}
      inputType="radio"
    />
  );
};

export default MultipleChoiceGridComponent;
