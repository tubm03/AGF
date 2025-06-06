export interface Message {
  id: number;
  text: string;
  user: string;
  timestamp?: Date;
}

export type SocketEvent =
  | "connect"
  | "disconnect"
  | "messages"
  | "new_message"
  | "user_typing";
