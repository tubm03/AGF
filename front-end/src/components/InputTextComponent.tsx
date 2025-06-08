import { useState } from "react";
import { useSurveyContext } from "../context/SurveyContext";

interface Props {
  listId: number;
  questionId: number;
  optionId: number;
}

const InputTextComponent = ({ listId, questionId, optionId }: Props) => {
  const { updateOptionValue, removeOption, updateOptionPercent } =
    useSurveyContext();
  const [value, setValue] = useState<string>();
  const [percent, setPercents] = useState(0);
  const handleRemoveOption = () => {
    removeOption(listId, questionId, optionId);
  };

  const handleValueChange = (newValue: string) => {
    setValue(newValue);
    updateOptionValue(listId, questionId, optionId, newValue);
  };

  const handlePercentChange = (newPercent: number) => {
    setPercents(newPercent);
    updateOptionPercent(listId, questionId, optionId, newPercent);
  };

  return (
    <div>
      value:{" "}
      <input
        type="text"
        value={value}
        onChange={(e) => handleValueChange(e.target.value)}
      />
      percent:{" "}
      <input
        style={{ width: "50px" }}
        type="number"
        value={percent}
        onChange={(e) => handlePercentChange(Number(e.target.value))}
      />
      <button onClick={handleRemoveOption}>-</button>
    </div>
  );
};

export default InputTextComponent;
