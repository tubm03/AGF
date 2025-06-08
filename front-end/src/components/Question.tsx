import type { Question } from "../types/Types";
import MultipleChoiceComponent from "./MultipleChoiceComponent";
import CheckboxComponent from "./CheckboxComponent";
import TitleComponent from "./TitleComponent";
import DropdownComponent from "./DropdownComponent";
import LinearScaleComponent from "./LinearScaleComponent";
import RatingComponent from "./RatingComponent";
import MultipleChoiceGridComponent from "./MultipleChoiceGridComponent";
import TickBoxGridComponent from "./TickBoxGridComponent";
import DateComponent from "./DateComponent";
import TimeComponent from "./TimeComponent";
import TextComponent from "./TextComponent";
import "../styles/styles.css";

interface Props {
  question: Question;
  questionId: number; // Optional prop to identify the question
  listId: number; // Optional prop to identify the list
}

const QuestionComponent = ({ question, questionId, listId }: Props) => {
  return (
    <div className="question">
      {question.type === "Title" && <TitleComponent question={question} />}
      {(question.type === "Short answer" || question.type === "Paragraph") && (
        <TextComponent
          listId={listId}
          questionId={questionId}
          question={question}
        />
      )}
      {question.type === "Multiple choice" && (
        <MultipleChoiceComponent
          question={question}
          questionId={questionId}
          listId={listId}
        />
      )}
      {question.type === "Checkboxes" && (
        <CheckboxComponent
          question={question}
          questionId={questionId}
          listId={listId}
        />
      )}
      {question.type === "Drop-down" && (
        <DropdownComponent
          listId={listId}
          question={question}
          questionId={questionId}
        ></DropdownComponent>
      )}
      {question.type === "Linear scale" && (
        <LinearScaleComponent
          question={question}
          listId={listId}
          questionId={questionId}
        />
      )}
      {question.type === "Rating" && (
        <RatingComponent
          question={question}
          listId={listId}
          questionId={questionId}
        />
      )}

      {question.type === "Multiple-choice grid" && (
        <MultipleChoiceGridComponent
          listId={listId}
          question={question}
          questionId={questionId}
        ></MultipleChoiceGridComponent>
      )}
      {question.type === "Tick box grid" && (
        <TickBoxGridComponent
          listId={listId}
          question={question}
          questionId={questionId}
        ></TickBoxGridComponent>
      )}
      {question.type === "Date" && (
        <DateComponent
          listId={listId}
          questionId={questionId}
          question={question}
        />
      )}
      {question.type === "Time" && (
        <TimeComponent
          listId={listId}
          questionId={questionId}
          question={question}
        />
      )}
    </div>
  );
};

export default QuestionComponent;
