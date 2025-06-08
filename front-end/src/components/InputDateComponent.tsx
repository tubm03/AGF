import { useState } from "react";
import { useSurveyContext } from "../context/SurveyContext";
import type { Option } from "../types/Types";

interface Props {
  listId: number;
  questionId: number;
  optionId: number;
  option: Option;
}

const InputDateComponent = ({
  listId,
  questionId,
  optionId,
  option,
}: Props) => {
  const { updateOptionValue, removeOption, updateOptionPercent } =
    useSurveyContext();
  const [value, setValue] = useState<string>(option.value || "");
  const [percent, setPercents] = useState(option.percent || 0);
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
        type="date"
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

export default InputDateComponent;
