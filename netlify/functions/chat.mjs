import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});

export default async (req) => {
  if (req.method !== "POST") {
    return Response.json({ error: "Method not allowed" }, { status: 405 });
  }

  try {
    const data = await req.json();
    const userMessage = (data.message || "").trim();

    if (!userMessage) {
      return Response.json({ error: "No message provided" }, { status: 400 });
    }

    const response = await ai.models.generateContent({
      model: "gemini-2.0-flash",
      contents: userMessage,
    });

    return Response.json({ response: response.text });
  } catch (e) {
    console.error("Error:", e.message);
    return Response.json({ error: e.message }, { status: 500 });
  }
};
