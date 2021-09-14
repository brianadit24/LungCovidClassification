# Lung Covid Classification using ResNet34
This is API for predict X-Ray Lung image to classify covid or normal.
## Tutorial

Clone the project

```bash
  git clone https://github.com/brianadit24/LungCovidClassification
```

Go to the project directory

```bash
  cd LungCovidClassification
```

Create and start API service

```bash
  docker-compose up
```

Stop and remove API service

```bash
  docker-compose down
```

  
## API Reference

Service: http://your-ip-address:8080

#### POST image

```http
  POST /predict
```
Content-Type: multipart/form-data
| Name    | Type   | Description                                         |
| :------ | :----- | :-------------------------------------------------- |
| `image` | `file` | **Required**. `image/jpeg` or `image/png` MIME Type |


## Result Example

**Input:**<br>
![Mask](results/mask.jpg)

**Output:**<br>
![Result_Mask](results/result_mask.jpg)

---

**Input:**<br>
![NoMask](results/no_mask.jpg)

**Output:**<br>
![Result_NoMask](results/no_mask_result.jpg) 
  
## Feedback

If you have any feedback, please reach out to us at brian.adityaherman@gmail.com

  
## 🔗 Contact Me
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/brianadityah/)

  
