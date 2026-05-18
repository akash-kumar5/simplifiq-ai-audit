"use client";

import axios from "axios";
import { useState } from "react";

export default function Home() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    company: "",
    website: "",
    industry: "",
    challenge: "",
  });

  const [loading, setLoading] = useState(false);

  const [message, setMessage] = useState("");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>,
  ) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    setLoading(true);

    setMessage("");

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/submit-lead",
        formData,
      );

      setMessage("AI Audit generated and emailed successfully.");

      console.log(response.data);
    } catch (error: any) {
      if (error.response?.data?.detail) {
        setMessage("Please enter valid information.");
      } else {
        setMessage("Something went wrong.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-black text-white flex items-center justify-center p-6">
      <div className="w-full max-w-2xl bg-zinc-900 p-8 rounded-2xl border border-zinc-800 shadow-2xl">
        <h1 className="text-4xl font-bold mb-3">AI Business Audit</h1>

        <p className="text-zinc-400 mb-8">
          Generate personalized AI automation insights for your business.
        </p>

        <form onSubmit={handleSubmit} className="space-y-5">
          <label className="text-sm text-zinc-400">Name *</label>
          <input
            type="text"
            name="name"
            placeholder="Your Name"
            onChange={handleChange}
            required
            className="w-full p-4 rounded-xl bg-zinc-800 border border-zinc-700 outline-none"
          />

          <label className="text-sm text-zinc-400">Your Email *</label>
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            onChange={handleChange}
            required
            className="w-full p-4 rounded-xl bg-zinc-800 border border-zinc-700 outline-none"
          />

          <label className="text-sm text-zinc-400">Company Name *</label>
          <input
            type="text"
            name="company"
            placeholder="Company Name"
            onChange={handleChange}
            required
            className="w-full p-4 rounded-xl bg-zinc-800 border border-zinc-700 outline-none"
          />

          <label className="text-sm text-zinc-400">Company Website *</label>
          <input
            type="text"
            name="website"
            placeholder="Company Website"
            onChange={handleChange}
            required
            className="w-full p-4 rounded-xl bg-zinc-800 border border-zinc-700 outline-none"
          />

          <input
            type="text"
            name="industry"
            placeholder="Industry"
            onChange={handleChange}
            className="w-full p-4 rounded-xl bg-zinc-800 border border-zinc-700 outline-none"
          />

          <textarea
            name="challenge"
            placeholder="What business challenge are you facing?"
            onChange={handleChange}
            rows={4}
            className="w-full p-4 rounded-xl bg-zinc-800 border border-zinc-700 outline-none"
          />
          <button
            type="submit"
            disabled={loading}
            className={`
    w-full py-4 rounded-xl font-semibold transition
    ${
      loading
        ? "bg-zinc-700 text-zinc-400 cursor-not-allowed"
        : "bg-white text-black hover:bg-zinc-300"
    }
  `}
          >
            {loading ? "Generating AI Audit..." : "Generate Audit Report"}
          </button>
        </form>

        {message && (
          <div className="mt-6 rounded-xl border border-zinc-700 bg-zinc-800 p-5 text-center">
            <p className="text-green-400 text-lg font-semibold">
              Audit Delivered Successfully
            </p>

            <p className="text-zinc-400 text-sm mt-2">
              Your AI-powered business audit report has been generated and
              emailed successfully.
            </p>

            <p className="text-zinc-500 text-xs mt-3">
              Please check your inbox and spam folder.
            </p>
          </div>
        )}
      </div>
    </main>
  );
}
