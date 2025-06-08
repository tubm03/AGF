// TickBoxGridComponent.tsx
import GridComponent from "./GridComponent";
import type { Question } from "../types/Types";

interface Props {
  question: Question;
  listId: number;
  questionId: number;
}

const TickBoxGridComponent = ({ question, listId, questionId }: Props) => {
  return (
    <GridComponent
      question={question}
      listId={listId}
      questionId={questionId}
      inputType="checkbox"
    />
  );
};

export default TickBoxGridComponent;
