# MindStudio GitHub Docs

本仓库汇总 MindStudio 相关工具的 Markdown 文档，根目录 README 作为统一入口，便于在 GitHub 和 Read the Docs 中浏览各工具文档。

## 文档入口

| 工具目录 | README |
| --- | --- |
| msdebug | [msdebug/README.md](msdebug/README.md) |
| msinsight | [msinsight/README.md](msinsight/README.md) |
| msit | [msit/README.md](msit/README.md) |
| mskl | [mskl/README.md](mskl/README.md) |
| mskpp | [mskpp/README.md](mskpp/README.md) |
| msmemscope | [msmemscope/README.md](msmemscope/README.md) |
| msmodeling | [msmodeling/README.md](msmodeling/README.md) |
| msmodelslim | [msmodelslim/README.md](msmodelslim/README.md) |
| msmonitor | [msmonitor/README.md](msmonitor/README.md) |
| msopcom | [msopcom/README.md](msopcom/README.md) |
| msopgen | [msopgen/README.md](msopgen/README.md) |
| msopmodeling | [msopmodeling/README.md](msopmodeling/README.md) |
| msopprof | [msopprof/README.md](msopprof/README.md) |
| msoptuner | [msoptuner/README.md](msoptuner/README.md) |
| msot | [msot/README.md](msot/README.md) |
| msprobe | [msprobe/README.md](msprobe/README.md) |
| msprof | [msprof/README.md](msprof/README.md) |
| msprof-analyze | [msprof-analyze/README.md](msprof-analyze/README.md) |
| mspti | [mspti/README.md](mspti/README.md) |
| mssanitizer | [mssanitizer/README.md](mssanitizer/README.md) |
| msserviceprofiler | [msserviceprofiler/README.md](msserviceprofiler/README.md) |
| mstt | [mstt/README.md](mstt/README.md) |
| mstx | [mstx/README.md](mstx/README.md) |

## Read the Docs 构建

本仓库使用 MkDocs 构建 Read the Docs 站点，关键文件如下：

- `mkdocs.yml`：MkDocs 站点配置与导航。
- `.readthedocs.yaml`：Read the Docs 构建配置。
- `requirements.txt`：MkDocs 构建依赖。

在 Read the Docs 导入仓库后，选择使用仓库根目录的 `.readthedocs.yaml` 构建即可。
