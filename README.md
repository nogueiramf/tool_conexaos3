<h1>
  <img src="https://avatars.githubusercontent.com/u/29469636?s=200&v=4" alt="Tool Conexão Amazon S3" style="width: 50px; height: 50px; vertical-align: middle; margin-right: 10px;" />
  Tool Conexão Amazon S3
</h1>

 Este projeto é destinado a configurar um sistema para upload de arquivos para um bucket S3 da AWS e realizar uma requisição POST para um serviço específico. Nosso objetivo é facilitar a gestão e transferência de arquivos para a nuvem e seu processamento subsequente.

## Instalação

Certifique-se de ter Python >=3.10 <=3.13 instalado em seu sistema. Este projeto utiliza `pip` para gerenciamento de dependências, oferecendo uma experiência de configuração e execução simples.

Primeiro, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```
## Personalização
Adicione suas credenciais da AWS e outras configurações no arquivo config.yaml

Modifique config.yaml para definir suas credenciais da AWS, informações do bucket, caminhos dos arquivos e URL de upload.
Execução do Projeto
Para criar um bucket S3 (se não existir), fazer upload de um arquivo e realizar uma requisição POST para o serviço, execute o seguinte comando a partir da pasta raiz do seu projeto:

```bash
python s3_file_uploader.py
```

## Configuração

Certifique-se de ter um arquivo `config.yaml` com a seguinte estrutura:

```yaml
aws_access_key: your_aws_access_key
aws_secret_key: your_aws_secret_key
region_name: your_aws_region
bucket_name: your_s3_bucket_name
file_path: path_to_your_file
s3_folder: ri-data-analysis/graphics
upload_url: http://store-files-service:39117/storage-files-service/upload
```

## Compreendendo o Workflow
O workflow é composto por dois componentes principais:

`S3Uploader`: Responsável por fazer o upload de arquivos para um bucket S3 da AWS. Se o bucket não existir, ele cria o bucket primeiro.

`UploadManager`: Responsável por realizar uma requisição POST para o serviço específico, passando o arquivo que foi feito upload para o S3.
Esses componentes trabalham juntos para garantir que seu arquivo seja carregado no S3 e, em seguida, devidamente processado pelo seu serviço.