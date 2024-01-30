# İris Tür Tahmini Uygulaması

Bu proje, popüler İris veri seti üzerinde eğitilmiş bir makine öğrenmesi modelini kullanarak, kullanıcıdan alınan çiçek ölçümlerine dayanarak İris çiçeğinin türünü tahmin eden bir web uygulamasıdır.

## Özellikler

- İris çiçeğinin sepal ve petal boyutlarına göre tür tahmini yapma.
- Farklı makine öğrenimi modelleri ile tahmin karşılaştırma.
- Streamlit ile interaktif web arayüzü.

## Başlarken

Bu bölüm, projeyi yerel geliştirme ortamınızda nasıl çalıştıracağınızı açıklar.

### Önkoşullar

Projeyi çalıştırmadan önce, Python'un yüklü olduğundan ve aşağıdaki Python paketlerinin yüklenmiş olduğundan emin olun:

- Flask
- Pandas
- Scikit-learn
- Streamlit
- Joblib
- Requests

Bu paketleri pip kullanarak yükleyebilirsiniz:

```bash
pip install flask pandas scikit-learn streamlit joblib requests
```

### Kurulum

1. Bu depoyu klonlayın:

```bash
git clone https://github.com/salimunlu/iris-ml-webapp.git
```

2. Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

3. Modeli eğitin ve joblib dosyalarını oluşturun (eğer repoda yoksa):

```bash
python train_model.py
```

Bu, gerekli `*.joblib` dosyalarını oluşturacaktır.

4. Flask API uygulamasını başlatın:

```bash
python app.py
```

Bu, API'nizi `http://localhost:5000` adresinde çalıştıracaktır.

5. Yeni bir terminal penceresi açın ve Streamlit uygulamasını çalıştırın:

```bash
streamlit run streamlit_app.py
```

Bu, web uygulamanızı `http://localhost:8501` adresinde çalıştıracaktır.

## Kullanım

Uygulama çalıştırıldığında, tarayıcınızda otomatik olarak açılacaktır. Eğer açılmazsa, Streamlit için `http://localhost:8501` ve Flask API için `http://localhost:5000` adreslerine gidin.

## Katkıda Bulunma

Projeye katkıda bulunmak istiyorsanız, lütfen öncelikle bir issue açarak veya mevcut issue'lara yorum yaparak başlayın.
