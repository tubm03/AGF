import type { Question } from "../types/Types";

interface Props {
  question: Question;
}

const TitleComponent = ({ question }: Props) => {
  return (
    <div>
      <h3>{question.heading}</h3>
    </div>
  );
};

export default TitleComponent;
