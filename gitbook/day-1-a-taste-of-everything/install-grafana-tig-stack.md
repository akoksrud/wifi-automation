# 20. Install Grafana / TIG-stack

To use InfluxQL we have to create a database connected to our bucket with the following one-liner

<pre class="language-bash" data-full-width="true"><code class="lang-bash"><strong>docker exec influxdb influx v1 dbrp create --db c9800-db --rp c9800-rp --bucket-id $(docker exec influxdb influx v1 dbrp list --org devnet --token ChangeMe2025! | grep "c9800-bucket" | awk '{print $3}') --default --org devnet --token ChangeMe2025!
</strong>
</code></pre>

If you want to see/do more in detail what is happening "under the hood", here is a more detailed process. Please note the number that is annotated in the output from the "list" command, and used in the "create" command

<pre class="language-bash" data-full-width="true"><code class="lang-bash">devnet-adm@ubuntu-devnet:~/tig-stack$ docker exec -it influxdb bash
root@71b07ba58958:/# influx v1 dbrp list --org devnet --token ChangeMe2025!
ID      Database        Bucket ID       Retention Policy        Default Organization ID

VIRTUAL DBRP MAPPINGS (READ-ONLY)
----------------------------------
ID                      Database        Bucket ID               Retention Policy        Default Organization ID
b53d2ec9d932635a        _monitoring     b53d2ec9d932635a        autogen                 true    6a6f13e3a65de450
09aac3a6cee8ab99        _tasks          09aac3a6cee8ab99        autogen                 true    6a6f13e3a65de450
574c74f705d86be2        c9800-bucket    <a data-footnote-ref href="#user-content-fn-1">7ccab63ed568ee68</a>      autogen                 true    6a6f13e3a65de450

root@71b07ba58958:/# influx v1 dbrp create --db c9800-db --rp c9800-rp --bucket-id <a data-footnote-ref href="#user-content-fn-2">7ccab63ed568ee68</a> --default --org devnet --token ChangeMe2025!

ID                      Database        Bucket ID               Retention Policy        Default Organization ID
0d94a420be168000        c9800-db        bc926b463de1d39a        c9800-rp                true    6a6f13e3a65de450

</code></pre>



[^1]: Copy this value to the line below. Your value will be different than this.

[^2]: use the value from above here
