import { API_URL } from "../../config/setting";
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useSurveyContext } from "../context/SurveyContext";
import "../styles/styles.css";

const Home = () => {
  const { formData, setFormData } = useSurveyContext();
  const [url, setUrl] = useState<string>("");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const navigate = useNavigate();
  const handleStartCrawl = async () => {
    if (!url) {
      return;
    }

    try {
      setIsLoading(true);
      await axios.post(`${API_URL}/crawl`, { url }).then((res) => {
        setFormData(res.data);
        console.log("Form data set in context:", formData);
      });
    } catch (error) {
      console.error("Crawl request failed:", error);
      setIsLoading(false);
    }
  };
  const handleCheckServer = async () => {
    try {
      const response = await axios.get(`${API_URL}/health`);
      console.log("Server response:", response.data);
    } catch (error) {
      console.error("Server check failed:", error);
    }
  };

  return (
    <div className="container">
      <h1>Web Crawler</h1>
      <div className="form-container">
        <div className="option-container">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter URL to crawl"
            disabled={isLoading}
          />
          <button onClick={handleStartCrawl} disabled={isLoading || !url}>
            {isLoading ? "Crawling..." : "Start Crawl"}
          </button>

          <button onClick={handleCheckServer}>Check Server Status</button>
          <button onClick={() => navigate("/survey")}>Go to Form</button>
        </div>

        {isLoading && (
          <div className="progress-container">
            {/* <div className="progress-bar" style={{ width: `${progress}%` }}></div> */}
            <div className="status">
              {/* {statusMessage} ({progress}%) - Time elapsed: {timeElapsed} */}
              <div className="loading-message">Crawling in progress...</div>
            </div>
          </div>
        )}

        <div className="form-data">
          <h2>Form Data</h2>
          {formData && <pre>{JSON.stringify(formData, null, 2)}</pre>}
        </div>
      </div>
    </div>
  );
};

export default Home;
