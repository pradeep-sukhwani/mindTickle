import os
import json


def main():
    html_structure = "<table>"
    with open(os.getcwd() + '/data 2') as file_obj:
        read_file = file_obj.read()
        json_data = json.loads(read_file)
        for key, value in json_data.items():
            if key == 'hits':
            	html_structure += "<tr><th style='border: 1px solid #ddd;'><td style='border: 1px solid #ddd; padding: 8px;'>Total Hit</td></th><th style='border: 1px solid #ddd;'><td style='border: 1px solid #ddd; padding: 8px;'>" + str(value.get('total')) + "</td></th></tr>"
            if key == 'aggregations':
                bucket_list = value.get('cname').get('buckets')
                for bucket_count, bucket in enumerate(bucket_list):
                    if bucket_count == 0:
                        html_structure += "<tr><td style='border: 1px solid #ddd;'>Bucket Key</td><td style='border: 1px solid #ddd;'>Completed</td><td style='border: 1px solid #ddd;'>Deactivated</td><td style='border: 1px solid #ddd;'>Active</td><td style='border: 1px solid #ddd;'>Added</td><td style='border: 1px solid #ddd;'>Submitted</td><td style='border: 1px solid #ddd;'>Total Doc Count</td></tr>"
                    else:
                        html_structure += "<tr><td style='border: 1px solid #ddd;'>" + str(bucket.get('key')) + "</td>"
                        m_state_dict = {}
                        for state in bucket.get('n').get('mstate').get('buckets'):
                            m_state_dict.update({state.get('key').lower(): str(state.get('doc_count'))})
                        html_structure += "<td style='border: 1px solid #ddd;'>" + m_state_dict.get('completed', '0') + "</td><td style='border: 1px solid #ddd;'>" + m_state_dict.get('deactivated', '0') + "</td><td style='border: 1px solid #ddd;'>" + m_state_dict.get('active', '0') + "</td><td style='border: 1px solid #ddd;'>" + m_state_dict.get('added', '0') + "</td><td style='border: 1px solid #ddd;'>" + m_state_dict.get('submitted', '0') + "</td><td style='border: 1px solid #ddd;'>" + str(bucket.get('doc_count')) + "</td>"
                        html_structure += "</tr>"
    with open(os.getcwd() + '/output2.html', "w") as html_file:
        html_file.write(html_structure)


if __name__ == '__main__':
    main()
