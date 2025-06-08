export interface Option {
  count: number;
  label: string;
  percent: number;
  xpath: string;
  value: string;
}

export interface Question {
  columns: [];
  heading: string;
  options: Option[];
  rows: [];
  scale: [];
  type: "Title" | "Short answer" | "Paragraph" | "Multiple choice" | "Checkboxes" | "Drop-down" | "Linear scale" | "Rating" | "Multiple-choice grid" | "Tick box grid" | "Date" | "Time"
  xpath: string;
}

export interface List {
  button: {
    value: string;
    xpath: string;
  };
  questions: Question[];
  xpath: string;
}

export interface Form {
  lists: List[];
  url: string;
}
