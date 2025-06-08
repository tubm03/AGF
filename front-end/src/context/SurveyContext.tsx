// context/SurveyContext.tsx
import { createContext, useContext, useState } from "react";
import type { Form, Option } from "../types/Types";
interface Props {
  children: React.ReactNode;
}

interface SurveyContextType {
  formData: Form | null;
  setFormData: React.Dispatch<React.SetStateAction<Form | null>>;
  updateOptionPercent: (
    listIndex: number,
    questionIndex: number,
    optionIndex: number,
    newPercent: number
  ) => void;
  updateOptionValue: (
    listIndex: number,
    questionIndex: number,
    optionIndex: number,
    newValue: string
  ) => void;
  addOption: (listIndex: number, questionIndex: number, option: Option) => void;
  removeOption: (
    listIndex: number,
    questionIndex: number,
    optionIndex: number
  ) => void;
}

const SurveyContext = createContext<SurveyContextType | undefined>(undefined);

export const SurveyProvider = ({ children }: Props) => {
  const [formData, setFormData] = useState<Form | null>(null);

  const updateOptionPercent = (
    listIndex: number,
    questionIndex: number,
    optionIndex: number,
    newPercent: number
  ) => {
    setFormData((prevFormData) => {
      if (!prevFormData) return null;

      return {
        ...prevFormData,
        lists: prevFormData.lists.map((list, lIdx) =>
          lIdx === listIndex
            ? {
                ...list,
                questions: list.questions.map((question, qIdx) =>
                  qIdx === questionIndex
                    ? {
                        ...question,
                        options: question.options.map((option, oIdx) =>
                          oIdx === optionIndex
                            ? { ...option, percent: newPercent }
                            : option
                        ),
                      }
                    : question
                ),
              }
            : list
        ),
      };
    });
  };

  const updateOptionValue = (
    listIndex: number,
    questionIndex: number,
    optionIndex: number,
    newValue: string
  ) => {
    setFormData((prevFormData) => {
      if (!prevFormData) return null;

      return {
        ...prevFormData,
        lists: prevFormData.lists.map((list, lIdx) =>
          lIdx === listIndex
            ? {
                ...list,
                questions: list.questions.map((question, qIdx) =>
                  qIdx === questionIndex
                    ? {
                        ...question,
                        options: question.options.map((option, oIdx) =>
                          oIdx === optionIndex
                            ? { ...option, value: newValue }
                            : option
                        ),
                      }
                    : question
                ),
              }
            : list
        ),
      };
    });
  };

  const addOption = (
    listIndex: number,
    questionIndex: number,
    option: Option
  ) => {
    setFormData((prevFormData) => {
      if (!prevFormData) return null;

      return {
        ...prevFormData,
        lists: prevFormData.lists.map((list, lIdx) =>
          lIdx === listIndex
            ? {
                ...list,
                questions: list.questions.map((question, qIdx) =>
                  qIdx === questionIndex
                    ? {
                        ...question,
                        options: [...question.options, option],
                      }
                    : question
                ),
              }
            : list
        ),
      };
    });
  };

  const removeOption = (
    listIndex: number,
    questionIndex: number,
    optionIndex: number
  ) => {
    setFormData((prevFormData) => {
      if (!prevFormData) return null;

      return {
        ...prevFormData,
        lists: prevFormData.lists.map((list, lIdx) =>
          lIdx === listIndex
            ? {
                ...list,
                questions: list.questions.map((question, qIdx) =>
                  qIdx === questionIndex
                    ? {
                        ...question,
                        options: question.options.filter(
                          (_, oIdx) => oIdx !== optionIndex
                        ),
                      }
                    : question
                ),
              }
            : list
        ),
      };
    });
  };

  return (
    <SurveyContext.Provider
      value={{
        formData,
        setFormData,
        updateOptionPercent,
        addOption,
        removeOption,
        updateOptionValue,
      }}
    >
      {children}
    </SurveyContext.Provider>
  );
};

export const useSurveyContext = () => {
  const context = useContext(SurveyContext);
  if (!context) {
    throw new Error("useSurvey must be used within SurveyProvider");
  }
  return context;
};
