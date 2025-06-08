import type { List } from "../types/Types";
import QuestionComponent from "./Question";

interface Props {
  list: List;
  listId: number; // Optional prop to identify the list
}

const ListQuestions = ({ list, listId }: Props) => {
  return (
    <div>
      {list.questions.map((question, index) => (
        <>
          <QuestionComponent
            listId={listId}
            question={question}
            questionId={index}
          ></QuestionComponent>
        </>
      ))}
    </div>
  );
};

export default ListQuestions;
